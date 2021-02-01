import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GroupsCardComponent } from './groups-card.component';

describe('GroupsCardComponent', () => {
  let component: GroupsCardComponent;
  let fixture: ComponentFixture<GroupsCardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GroupsCardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GroupsCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
