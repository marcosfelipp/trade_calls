import { Component, OnInit } from '@angular/core';
import { Call } from '../../models/Call';
import { CallService} from '../../services/call.service';

@Component({
  selector: 'app-calls',
  templateUrl: './calls.component.html',
  styleUrls: ['./calls.component.css']
})
export class CallsComponent implements OnInit {
  call: Call;
  constructor(private callService: CallService) { }

  ngOnInit(): void {
  }

  sendCall(){
    this.callService.postCalls(this.call);
  }
}
