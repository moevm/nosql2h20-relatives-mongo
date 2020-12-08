import React, { useState } from "react";
import {Modal, Button, Container, Row, Col, Form} from "react-bootstrap";
import axios from 'axios'

export default function ModalGetPerson({text}) {


        const [show, setShow] = useState(false);
        const handleClose = () => setShow(false);
        const handleShow = () => setShow(true);

        axios.get("/api/persons_list")
        .then(response => console.log("response", response.data))

        return (
          <>
            <Button variant="light" onClick={handleShow}>
              {text}
            </Button>


            <Modal show={show} onHide={handleClose}>
              <Modal.Header closeButton>
                <Modal.Title>Get Person</Modal.Title>
              </Modal.Header>
              <Modal.Body>
                  <Form.Group controlId="Parents">
                    <Form.Label>Change person &nbsp;</Form.Label>
                    <Form.Control as="select" custom>
                      <option>Иванова И.А</option>
                      <option>Иванова И.Б</option>
                      <option>Иванова И.В</option>
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
