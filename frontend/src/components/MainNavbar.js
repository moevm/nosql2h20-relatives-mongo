import React from "react";
import {Nav, Navbar, Modal, Col} from "react-bootstrap";
import {Link} from "react-router-dom";
import ModalAddDynasty from "./ModalAddDynasty.js";
import ModalAddPerson from "./ModalAddPerson.js";
import ModalImport from "./ModalImport.js";
import ModalExport from "./ModalExport.js";
import ModalGetPerson from "./ModalGetPerson.js";
import ModalGetDynasty from "./ModalGetDynasty.js";
import ModalCrosses from "./ModalCrosses.js";


export default function MainNavbar() {
    return (
      <>
        <Navbar bg="dark" variant="dark" expand="lg">
            <Navbar.Brand as={Link} to="/">
                <i>Relatives</i>
            </Navbar.Brand>
            <Nav defaultActiveKey="/">
                <Nav.Item>
                    <ModalAddDynasty>Add Dynasty</ModalAddDynasty> &nbsp;
                </Nav.Item>
                <Nav.Item>
                    <ModalAddPerson>Add Person</ModalAddPerson> &nbsp;
                </Nav.Item>
                <Nav.Item>
                    <ModalImport text="Import"></ModalImport> &nbsp;
                </Nav.Item>
                <Nav.Item>
                    <ModalExport text="Export"></ModalExport> &nbsp;
                </Nav.Item>
            </Nav>
        </Navbar>

        <Navbar bg="secondary" >
            <Nav defaultActiveKey="/" className="text-white">
                <Nav.Item>
                    <Nav.Link as={Link} to="/api/fulltree" className="text-white">Full Tree</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <ModalGetPerson text="Parents"></ModalGetPerson> &nbsp;
                </Nav.Item>
                <Nav.Item>
                    <ModalGetPerson text="Childs"></ModalGetPerson> &nbsp;
                </Nav.Item>
                <Nav.Item>
                    <ModalGetDynasty text="Childs"></ModalGetDynasty> &nbsp;
                </Nav.Item>
                <Nav.Item>
                    <ModalCrosses text="Childs"></ModalCrosses> &nbsp;
                </Nav.Item>
            </Nav>
        </Navbar>
        </>
    );

}
