import { Component, OnInit } from '@angular/core';

import { TopicService } from '../topic.service';
import {Topics, Posts} from '../interfaces';

import {PostService} from '../post.service';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  topics: Topics[] = [];
  posts: Posts[] = [];
  constructor(private topicService: TopicService, private postService: PostService) { }
  ngOnInit(): void {
    this.getTopics();
    this.getPosts();

  }
  getPosts() {
    this.postService.getPosts().subscribe((data) => {
      this.posts = data;
    });
  }
  getTopics() {
    this.topicService.getTopics().subscribe((data) => {
      this.topics = data;
    });
  }
}
