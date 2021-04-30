import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs/internal/Observable';
import {Comments, Posts, Topics} from './interfaces';
@Injectable({
  providedIn: 'root'
})
export class PostService {
  BASE_URL = 'http://localhost:8000';
  constructor(private http: HttpClient) { }
  getPosts(): Observable<Posts[]> {
    return this.http.get<Posts[]>(`${this.BASE_URL}/api/posts`);
  }
  createPost(post: Posts): Observable<Posts[]> {
    return this.http.post<Posts[]>(`${this.BASE_URL}/api/posts/`, post);
  }
  getPostsByTopic(id): Observable<Posts[]>{
    return this.http.get<Posts[]>(`${this.BASE_URL}/api/postsTopicId/${id}`);
  }
  getComments(id): Observable<Comments[]> {
    return this.http.get<Comments[]>(`${this.BASE_URL}/api/commentsPostId/${id}`);
  }
  createComment(comment: Comments): Observable<Comments[]> {
    return this.http.post<Comments[]>(`${this.BASE_URL}/api/comments/`, comment);
  }
}
