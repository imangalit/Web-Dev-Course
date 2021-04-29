import { Component, OnInit } from '@angular/core';
import {topics} from '../database';

import { TopicService } from '../topic.service';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  topics = topics;
  popTopics;
  constructor(private topicService: TopicService) { }

  ngOnInit(): void {
    this.getPop()
  }

  getPop(): void {
    this.popTopics = this.topicService.getPop();
  }
}
