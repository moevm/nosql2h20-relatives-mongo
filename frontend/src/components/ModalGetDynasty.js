import React, { useState } from "react";
import {Modal, Button, Container, Row, Col, Form} from "react-bootstrap";
import axios from 'axios'

export default function ModalGetDynasty() {


        const [show, setShow] = useState(false);
        const handleClose = () => setShow(false);
        const handleShow = () => setShow(true);

        axios.get("/api/dynasty_list")
        .then(response => console.log("response", response.data))

        return (
          <>
            <Button variant="light" onClick={handleShow}>
              Show Dynasty
            </Button>


            <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
              <Modal.Title>Get Dynasty</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form.Group controlId="Parents">
                  <Form.Label>Choose dynasty &nbsp;</Form.Label>
                  <Form.Control as="select" custom>
                    <option>Токаревичи</option>
                    <option>Петровичи</option>
                    <option>Государичи</option>
                    <option>Марковичи</option>
                    </Form.Control>
                  </Form.Group>
              </Modal.Body>
              <Modal.Footer>
                <Button variant="secondary" onClick={handleClose}>
                  Close
                </Button>
                <Button variant="primary" onClick={handleClose}>
                  Build
                </Button>
              </Modal.Footer>
            </Modal>
          </>
        );

}
