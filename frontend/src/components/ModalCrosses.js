import React, { useState } from "react";
import {Modal, Button, Container, Row, Col, Form} from "react-bootstrap";

export default function ModalCrosses() {


        const [show, setShow] = useState(false);
        const handleClose = () => setShow(false);
        const handleShow = () => setShow(true);

        return (
          <>
            <Button variant="light" onClick={handleShow}>
              Find Crosses
            </Button>


            <Modal show={show} onHide={handleClose}>
              <Modal.Header closeButton>
                <Modal.Title>Get Dynasty</Modal.Title>
              </Modal.Header>
              <Modal.Body>
              <Form inline>
                  <Form.Group controlId="Parents">
                    <Form.Label>Choose dynasty 1 &nbsp;</Form.Label>
                    <Form.Control as="select" custom>
                      <option>Токаревичи</option>
                      <option>Государичи</option>
                      <option>Марковичи</option>
                    </Form.Control>
                  </Form.Group>

                      <Form.Group controlId="Parents">
                        <Form.Label>Choose dynasty 2 &nbsp;</Form.Label>
                        <Form.Control as="select" custom>
                          <option>Государичи</option>
                          <option>Марковичи</option>
                            <option>Петровичи</option>
                        </Form.Control>
                      </Form.Group>
                      </Form>
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
