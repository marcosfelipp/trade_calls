import { Component, OnInit } from '@angular/core';
import {CallService} from '../../services/call.service';
import {Call} from '../../models/Call';

@Component({
  selector: 'app-calls-list',
  templateUrl: './calls-list.component.html',
  styleUrls: ['./calls-list.component.css']
})
export class CallsListComponent implements OnInit {
  calls: Call[];
  constructor(private callService: CallService) { }

  ngOnInit(): void {
    this.setCalls();
  }

  setCalls(){
    this.callService.getCalls().subscribe(calls => {
      this.calls = calls;
    });
  }
}
