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
    this.callService.getCalls("5ec3d12a0af0cca40e8c3d51").subscribe(calls => {
      this.calls = calls;
    });
  }
}
