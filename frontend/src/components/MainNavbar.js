import React from "react";
import {Nav, Navbar} from "react-bootstrap";
import {Link} from "react-router-dom";

export default function MainNavbar() {
    return (
      <>
        <Navbar bg="dark" variant="dark">
            <Navbar.Brand as={Link} to="/">
                <i>Relatives</i>
            </Navbar.Brand>
            <Nav defaultActiveKey="/">
                <Nav.Item>
                    <Nav.Link as={Link} to="/">Home</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link as={Link} to="/stat">Stat</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link as={Link} to="/traffic">Traffic</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link as={Link} to="/data">Data</Nav.Link>
                </Nav.Item>
            </Nav>
        </Navbar>

        <Navbar bg="secondary" >
            <Nav defaultActiveKey="/" className="text-white">
                <Nav.Item>
                    <Nav.Link as={Link} to="/" className="text-white">Full Tree</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link as={Link} to="/stat" className="text-white">Parents</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link as={Link} to="/traffic" className="text-white">Childs</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link as={Link} to="/data" className="text-white">Sort Childs</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link as={Link} to="/data" className="text-white">Show Dynasty</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link as={Link} to="/data" className="text-white">Find Crosses</Nav.Link>
                </Nav.Item>
            </Nav>
        </Navbar>
        </>
    );

}
