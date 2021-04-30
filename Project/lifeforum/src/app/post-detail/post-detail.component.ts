import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {PostService} from '../post.service';
import {Posts} from '../interfaces';

@Component({
  selector: 'app-post-detail',
  templateUrl: './post-detail.component.html',
  styleUrls: ['./post-detail.component.css']
})
export class PostDetailComponent implements OnInit {
  post;
  posts: Posts[] = [];
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
    this.getPosts();
    this.likesCount = 0;
    this.dislikesCount = 0;
    this.comments=[""];
  }

  getPosts(): void {
    this.postService.getPosts().subscribe((data) => {
      this.posts = data;
      this.post = this.posts.find(post => post.id === Number(this.route.snapshot.paramMap.get('postId')));
      console.log(this.post);
    });
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
