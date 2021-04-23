import { Component, OnInit } from '@angular/core';
import {posts} from '../database';
import { ActivatedRoute } from '@angular/router';
import {PostService} from '../post.service';

@Component({
  selector: 'app-post-detail',
  templateUrl: './post-detail.component.html',
  styleUrls: ['./post-detail.component.css']
})
export class PostDetailComponent implements OnInit {
  post;
  text: string = '';
  comments: string[];

  likesCount: number;
  isActiveLike: boolean;
  isActiveDislike: boolean;
  dislikesCount: number;

  constructor(
    private postService: PostService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit() {
    const routeParams = this.route.snapshot.paramMap;
    const postIdFromRoute = Number(routeParams.get('postId'));
    // Find the product that correspond with the id provided in route.
    this.post = posts.find(post => post.id === postIdFromRoute);
    this.likesCount = 0;
    this.dislikesCount = 0;
    //this.comments.push("hello");
  }
  like() {
    this.likesCount += (this.isActiveLike) ? -1 : 1;
    this.isActiveLike = !this.isActiveLike;
  }
  dislike() {
    this.dislikesCount += (this.isActiveDislike) ? -1 : 1;
    this.isActiveDislike = !this.isActiveDislike;
  }
  appendComment(comment): void {
    this.comments.push(comment);
  }

}
