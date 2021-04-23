import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { topics } from '../database';
import { PostService } from '../post.service';

@Component({
  selector: 'app-topic-detail',
  templateUrl: './topic-detail.component.html',
  styleUrls: ['./topic-detail.component.css']
})

export class TopicDetailComponent implements OnInit {
  topic;
  posts;
  constructor(
    private route: ActivatedRoute,
    private postService: PostService,
  ) { }

  ngOnInit() {
    const routeParams = this.route.snapshot.paramMap;
    const topicIdFromRoute = Number(routeParams.get('topicId'));
    // Find the product that correspond with the id provided in route.
    this.topic = topics.find(topic => topic.id === topicIdFromRoute);
    this.getPosts();
  }
  getPosts(): void {
    this.posts = this.postService.getPostByCategory(this.topic.id);
  }
}
