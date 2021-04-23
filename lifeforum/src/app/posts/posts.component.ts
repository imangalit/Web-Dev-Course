import { Component, OnInit } from '@angular/core';
import {PostService} from '../post.service';
import {posts} from '../database';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})
export class PostsComponent implements OnInit {
  latestTopics;
  constructor(private postService: PostService) { }

  ngOnInit(): void {
    this.getLatest();
  }

  getLatest(): void {
    this.latestTopics = this.postService.getLatest();
  }
}
