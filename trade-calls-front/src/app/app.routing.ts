import {RouterModule, Routes} from '@angular/router';
import {HomeComponent} from './components/home/home.component';
import {GroupComponent} from './components/group/group.component';
import {ModuleWithProviders} from '@angular/core';

const APP_ROUTES: Routes = [
  { path: '' , component: HomeComponent },
  { path: 'group', component: GroupComponent}
];

export const routing: ModuleWithProviders = RouterModule.forRoot(APP_ROUTES);
