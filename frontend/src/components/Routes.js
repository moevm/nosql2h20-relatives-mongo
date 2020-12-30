import React from "react";
import {Route, Switch} from "react-router-dom";
import Home from "../pages/Home";
import Export from "../pages/Export";

export default function Routes() {
    return (
        <Switch>
            <Route exact path="/" component={Home}/>
            <Route path="/export" component={Export}/>
        </Switch>
    );
}
