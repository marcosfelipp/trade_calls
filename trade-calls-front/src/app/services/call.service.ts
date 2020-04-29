import { Injectable } from '@angular/core';
import {Call} from '../models/Call';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CallService {
  private callsUrl = 'http://0.0.0.0:5000/api/v1/call';

  constructor(private http: HttpClient) { }

  getCalls(): Observable<Call[]>{
    return this.http.get<Call[]>(this.callsUrl);
  }

  postCalls(call: Call): Observable<any>{
    console.log(call);
    return this.http.post<any>(this.callsUrl, call);
  }
}
