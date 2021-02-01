import { Injectable } from '@angular/core';
import { Group} from '../models/Group';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GroupService {

  private groupUrl = 'http://192.168.99.100:30000/api/v1/groups/60180f5f2a2b1a453eb99ef1';

  constructor(private http: HttpClient) { }

  getGroup(): Observable<Group[]>{
    return this.http.get<Group[]>(this.groupUrl);
  }

  postGroup(group: Group): Observable<any>{
    console.log(group);
    return this.http.post<any>(this.groupUrl, Group);
  }
}
