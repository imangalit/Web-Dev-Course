import { Component, OnInit } from '@angular/core';
import {topics} from '../database';

@Component({
  selector: 'app-topics',
  templateUrl: './topics.component.html',
  styleUrls: ['./topics.component.css']
})
export class TopicsComponent implements OnInit {
  topics = topics;
  constructor() { }
  ngOnInit(): void {
  }
}
