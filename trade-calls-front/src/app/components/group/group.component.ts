import { Component, OnInit, OnDestroy } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {Subscription} from 'rxjs';

@Component({
  selector: 'app-group',
  templateUrl: './group.component.html',
  styleUrls: ['./group.component.css']
})
export class GroupComponent implements OnInit {

  subscription: Subscription;
  id: string;

  constructor(private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.subscription = this.route.params.subscribe(
      (params: any) => {
       this.id = params.id;
      }
    );
  }

  ngOnDestroy(): void{
    this.subscription.unsubscribe();
  }

  getGroupInfo(): void{

  }

}
