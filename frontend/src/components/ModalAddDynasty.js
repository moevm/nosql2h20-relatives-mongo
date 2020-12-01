import React, { useState } from "react";
import {Modal, Button, Container, Row, Col, Form} from "react-bootstrap";

export default function ModalAddDynasty() {

      const [show, setShow] = useState(false);
      const handleClose = () => setShow(false);
      const handleShow = () => setShow(true);

      return (
        <>
          <Button variant="light" onClick={handleShow}>
            Add Dynasty
          </Button>


          <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
              <Modal.Title>Add New Dynasty</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form.Label>Dynasty Name</Form.Label>
                <Form.Control placeholder="Enter name" />
            </Modal.Body>
            <Modal.Footer>
              <Button variant="secondary" onClick={handleClose}>
                Close
              </Button>
              <Button variant="primary" onClick={handleClose}>
                Next
              </Button>
            </Modal.Footer>
          </Modal>
        </>
      );


}
