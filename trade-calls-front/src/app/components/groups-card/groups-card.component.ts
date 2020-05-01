import { Component, OnInit } from '@angular/core';
import {GroupService} from '../../services/group.service';
import {Group} from '../../models/Group';

@Component({
  selector: 'app-groups-card',
  templateUrl: './groups-card.component.html',
  styleUrls: ['./groups-card.component.css']
})
export class GroupsCardComponent implements OnInit {
  groups: Group[];

  constructor(private groupSevice: GroupService) { }

  ngOnInit(): void {
    this.setGroups();
  }

  setGroups(){
    this.groupSevice.getGroup().subscribe(groups => {
      this.groups = groups;
      console.log(groups);
    });
  }
}
