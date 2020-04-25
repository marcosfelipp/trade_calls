import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CallsComponent } from './components/calls/calls.component';
import { NewCallComponent } from './components/new-call/new-call.component';

@NgModule({
  declarations: [
    AppComponent,
    CallsComponent,
    NewCallComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
