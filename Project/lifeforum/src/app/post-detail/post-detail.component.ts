import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {PostService} from '../post.service';
import {Posts, Comments} from '../interfaces';

@Component({
  selector: 'app-post-detail',
  templateUrl: './post-detail.component.html',
  styleUrls: ['./post-detail.component.css']
})
export class PostDetailComponent implements OnInit {
  post;
  posts: Posts[] = [];
  text: string = '';
  comments: Comments[] = [];

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
  }
  getComments(id) {
    this.postService.getComments(id).subscribe((data) => {
      this.comments = data;
      console.log(this.comments);
    });
  }
  getPosts(): void {
    this.postService.getPosts().subscribe((data) => {
      this.posts = data;
      this.post = this.posts.find(post => post.id === Number(this.route.snapshot.paramMap.get('postId')));
      console.log(this.post);
      this.getComments(this.post.id);
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
  appendComment(desc) {
    const comment = {
      description: desc,
      post_id: this.post.id,
      id: undefined
    };
    console.log(this.post.id);
    this.postService.createComment(comment).subscribe((data) => {
      console.log(data);
    });
    window.location.reload();
  }
}
