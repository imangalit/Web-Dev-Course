import { Injectable } from '@angular/core';
import {topics} from './database';

@Injectable({
  providedIn: 'root'
})
export class TopicService {

  constructor() { }
  getPop(): any{
    const res = topics.filter(topic => topic.rating > 0);
    return res;
  }
}
