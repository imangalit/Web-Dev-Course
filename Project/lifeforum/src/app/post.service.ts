import { Injectable } from '@angular/core';
import {posts} from './database';
@Injectable({
  providedIn: 'root'
})
export class PostService {
  constructor() { }
  getPostByCategory(topicId): any{
    const res = posts.filter(post => post.topicId === topicId);
    return res;
  }
  getLatest(): any{
    const res = posts;
    return res;
  }
}
