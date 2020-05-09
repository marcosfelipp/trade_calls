import { Injectable } from '@angular/core';
import { Group} from '../models/Group';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GroupService {

  private groupUrl = 'http://0.0.0.0:5000/api/v1/groups/5eb6ed1957e1a77f1c10a49c';

  constructor(private http: HttpClient) { }

  getGroup(): Observable<Group[]>{
    return this.http.get<Group[]>(this.groupUrl);
  }

  postGroup(group: Group): Observable<any>{
    console.log(group);
    return this.http.post<any>(this.groupUrl, Group);
  }
}
