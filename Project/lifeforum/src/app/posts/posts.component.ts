import { Component, OnInit } from '@angular/core';
import {PostService} from '../post.service';
import {Posts, Topics} from '../interfaces';
import {TopicService} from '../topic.service';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})
export class PostsComponent implements OnInit {
  posts: Posts[] = [];
  constructor(private postService: PostService) { }
  ngOnInit(): void {
    this.getPosts();
  }
  getPosts() {
    this.postService.getPosts().subscribe((data) => {
      this.posts = data;
    });
  }
}
