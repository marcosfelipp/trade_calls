import {Component, OnInit} from '@angular/core';
import {Call} from '../../models/Call';
import {CallService} from '../../services/call.service';
import {FormGroup, FormControl} from '@angular/forms';
import {ViewChild } from '@angular/core';

@Component({
  selector: 'app-calls',
  templateUrl: './calls.component.html',
  styleUrls: ['./calls.component.css']
})
export class CallsComponent implements OnInit {
  formCall: FormGroup;
  @ViewChild('closebutton') closebutton;
  constructor(private callService: CallService) {
  }

  ngOnInit(): void {
    this.createForm(new Call());
  }

  createForm(call: Call) {
    this.formCall = new FormGroup({
      ativo: new FormControl(call.stock),
      tipo: new FormControl(call.callType),
      entrada: new FormControl(call.start),
      stopLoss: new FormControl(call.stopLoss),
      stopGain: new FormControl(call.stopGain),
      description: new FormControl(call.description)
    });
  }

  onSubmit() {
    console.log(this.formCall.value);
    this.sendCall(this.formCall.value);
  }

  sendCall(call) {
    this.callService.postCalls(call).subscribe(res => {
      console.log(res);
      this.formCall.reset(new Call());
      this.closebutton.nativeElement.click();
    });
  }
}
