import React, { useState } from "react";
import {Modal, Button, Container, Row, Col,Form} from "react-bootstrap";

export default function ModalAddPerson() {

      const [show, setShow] = useState(false);
      const handleClose = () => setShow(false);
      const handleShow = () => setShow(true);

      return (
        <>
          <Button variant="light" onClick={handleShow}>
            Add Person
          </Button>


          <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
              <Modal.Title>New Person</Modal.Title>
            </Modal.Header>
            <Modal.Body>
              <Form.Group controlId="Name">
                <Form.Label>First&Last Name</Form.Label>
                <Form.Control placeholder="Enter name" />
              </Form.Group>
                <Form.Group controlId="BY">
                  <Form.Label>Birth year</Form.Label>
                  <Form.Control placeholder="1900" />
                </Form.Group>
                  <Form.Group controlId="DY">
                    <Form.Label>Death year</Form.Label>
                    <Form.Control placeholder="2000" />
                  </Form.Group>
                  <Form inline>
                    <Form.Group controlId="Parents">
                      <Form.Label>Mother &nbsp;</Form.Label>
                      <Form.Control as="select" custom>
                        <option>Иванова И.А</option>
                        <option>Иванова И.Б</option>
                        <option>Иванова И.В</option>
                      </Form.Control>
                    </Form.Group>
                    <Form.Group controlId="Parents">
                      <Form.Label>&nbsp;Father&nbsp;</Form.Label>
                      <Form.Control as="select" custom>
                        <option>Лапохни И.А</option>
                        <option>Ковальски И.Б</option>
                        <option>Ноэль Г.В</option>
                      </Form.Control>
                    </Form.Group>
                    </Form>
            </Modal.Body>
            <Modal.Footer>
              <Button variant="secondary" onClick={handleClose}>
                Close
              </Button>
              <Button variant="primary" onClick={handleClose}>
                Save Changes
              </Button>
            </Modal.Footer>
          </Modal>
        </>
      );


}
