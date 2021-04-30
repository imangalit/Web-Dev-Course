import { Component, OnInit } from '@angular/core';
import { Topics } from '../interfaces';
import {TopicService} from '../topic.service';

@Component({
  selector: 'app-topics',
  templateUrl: './topics.component.html',
  styleUrls: ['./topics.component.css']
})
export class TopicsComponent implements OnInit {
  topics: Topics[] = [];
  topicTitle: string = '';
  logged = false;
  
  constructor(private topicService: TopicService) { }
  ngOnInit(): void {
    this.getTopics();
  }
  createTopic() {
    const topic = {
      title: this.topicTitle,
      id: undefined
    };

    this.topicService.createTopic(topic).subscribe((data) => {
      console.log(data);
    });
  }
  getTopics() {
    this.topicService.getTopics().subscribe((data) => {
      this.topics = data;
    });
  }
}
