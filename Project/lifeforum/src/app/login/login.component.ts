import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import {Router} from '@angular/router';
import {User} from '../interfaces';
import { Location } from '@angular/common';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  user ?: User;
  logged = false;
  username = '';
  password = '';
  constructor(private router: Router, private authService: AuthService, private location: Location){}

  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }
  login() {
    this.authService.login(this.username, this.password).subscribe((data) => {

      localStorage.setItem('token', data.token);
      this.logged = true;

      this.username = '';
      this.password = '';
      this.router.navigate(['']);
    });
  }
  logout() {
    this.username = '';
    this.password = '';
    this.logged = false;
    localStorage.removeItem('token');
  }
}
