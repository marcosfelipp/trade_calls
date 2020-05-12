import { Injectable } from '@angular/core';
import { Group} from '../models/Group';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GroupService {

  private groupUrl = 'http://0.0.0.0:5000/api/v1/groups/5ebaa35f45bfeb3f5118d304';

  constructor(private http: HttpClient) { }

  getGroup(): Observable<Group[]>{
    return this.http.get<Group[]>(this.groupUrl);
  }

  postGroup(group: Group): Observable<any>{
    console.log(group);
    return this.http.post<any>(this.groupUrl, Group);
  }
}
