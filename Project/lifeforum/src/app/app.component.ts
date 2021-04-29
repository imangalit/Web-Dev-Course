import { Component } from '@angular/core';
import{AuthService} from './auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'lifeforum';
  logged = false;
  username = '';
  password = '';
  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }
  constructor(private authService: AuthService) {
  }

  login() {
    this.authService.login(this.username, this.password).subscribe((data) => {

      localStorage.setItem('token', data.token);

      this.logged = true;
      this.username = '';
      this.password = '';
    });
  }

  logout(){
    this.logged = false;
    localStorage.removeItem('token');
  }
}
