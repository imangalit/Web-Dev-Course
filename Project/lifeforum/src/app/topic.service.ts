import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs/internal/Observable';
import {AuthToken, Topics} from './interfaces';

@Injectable({
  providedIn: 'root'
})
export class TopicService {
  BASE_URL = 'http://localhost:8000';
  constructor(private http: HttpClient) { }
  getTopics(): Observable<Topics[]> {
    return this.http.get<Topics[]>(`${this.BASE_URL}/api/topics`);
  }
  createTopic(topic: Topics): Observable<Topics[]> {
    return this.http.post<Topics[]>(`${this.BASE_URL}/api/topics/`, topic);
  }
}
