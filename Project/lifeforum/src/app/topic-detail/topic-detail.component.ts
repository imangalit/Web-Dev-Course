import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { PostService } from '../post.service';
import {Posts, Topics} from '../interfaces';
import {TopicService} from '../topic.service';

@Component({
  selector: 'app-topic-detail',
  templateUrl: './topic-detail.component.html',
  styleUrls: ['./topic-detail.component.css']
})

export class TopicDetailComponent implements OnInit {
  topics: Topics[] = [];
  topic;
  posts: Posts[] = [];
  postTitle: string = '';
  postText: string = '';

  constructor(
    private route: ActivatedRoute,
    private postService: PostService,
    private topicService: TopicService,
  ) { }

  ngOnInit() {
    // Find the product that correspond with the id provided in route.
    this.getTopics();
  }
  getTopics() {
    this.topicService.getTopics().subscribe((data) => {
      this.topics = data;
      this.topic = this.topics.find(topic => topic.id === Number(this.route.snapshot.paramMap.get('topicId')));
      this.getPostsByTopic(this.topic.id);
    });
  }
  getPostsByTopic(id) {
    this.postService.getPostsByTopic(id).subscribe((data) => {
      this.posts = data;
    });
  }

  newPost() {
    const post = {
      name: this.postTitle,
      description: this.postText,
      topic_id: this.topic.id,
      id: undefined
    };

    this.postService.createPost(post).subscribe((data) => {
      console.log(data);
    });
  }
}
