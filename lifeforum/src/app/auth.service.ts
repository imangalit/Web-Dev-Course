import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable, of} from 'rxjs';
import {AuthToken} from './interfaces';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  BASE_URl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }
  login(username: string, password: string): Observable<AuthToken> {
    return this.http.post<AuthToken>(`${this.BASE_URl}/api/login/`, {
      username,
      password
    });
  }
}
