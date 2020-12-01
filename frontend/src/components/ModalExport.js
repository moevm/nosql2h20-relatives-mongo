import React, { useState } from "react";
import {Modal, Button, Container, Row, Col, Form} from "react-bootstrap";

export default function ModalExport() {


        const [show, setShow] = useState(false);
        const handleClose = () => setShow(false);
        const handleShow = () => setShow(true);

        return (
          <>
            <Button variant="light" onClick={handleShow}>
              Export
            </Button>


            <Modal show={show} onHide={handleClose}>
              <Modal.Header closeButton>
                <Modal.Title>Save tree</Modal.Title>
              </Modal.Header>
              <Modal.Body>
                  <Form.Label>Input abs path to save file</Form.Label>
                  <Form.Control placeholder="Enter path" />
              </Modal.Body>
              <Modal.Footer>
                <Button variant="secondary" onClick={handleClose}>
                  Close
                </Button>
                <Button variant="primary" onClick={handleClose}>
                  Export
                </Button>
              </Modal.Footer>
            </Modal>
          </>
        );

}
