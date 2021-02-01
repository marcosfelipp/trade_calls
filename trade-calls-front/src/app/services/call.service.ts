import { Injectable } from '@angular/core';
import {Call} from '../models/Call';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CallService {
  private callsUrl = 'http://192.168.99.100:30000/api/v1/calls/';

  constructor(private http: HttpClient) { }

  getCalls(groupID: string): Observable<Call[]>{
    return this.http.get<Call[]>(this.callsUrl + groupID);
  }

  postCalls(call: Call): Observable<any>{
    console.log(call);
    return this.http.post<any>(this.callsUrl, call);
  }
}
