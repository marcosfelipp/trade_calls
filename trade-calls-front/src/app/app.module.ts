import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule} from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CallsComponent } from './components/calls/calls.component';
import { NewCallComponent } from './components/new-call/new-call.component';
import { MenuComponent } from './components/menu/menu.component';
import { CallsListComponent } from './components/calls-list/calls-list.component';
import { ReactiveFormsModule } from '@angular/forms';
import { GroupsCardComponent } from './components/groups-card/groups-card.component';
import { GroupComponent } from './components/group/group.component';
import { OverviewComponent } from './components/overview/overview.component';

@NgModule({
  declarations: [
    AppComponent,
    CallsComponent,
    NewCallComponent,
    MenuComponent,
    CallsListComponent,
    GroupsCardComponent,
    GroupComponent,
    OverviewComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
