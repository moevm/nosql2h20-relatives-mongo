import React, { useState } from "react";
import {Modal, Button, Container, Row, Col, Form} from "react-bootstrap";
import axios from 'axios'


export default function ModalExport() {

        const writeJsonFile = require('write-json-file');

        const [show, setShow] = useState(false);
        const [resp, setData] = useState("fqwqd");
        const [path, setPath] = useState("");
        const handleClose = () => setShow(false);
        const handleShow = () => setShow(true);

//        axios.get("/api/fulltree")
//        .then(response => setData(JSON.stringify(response.data)) )

        setData("her")

        return (
          <>
            <Button variant="light" onClick={handleShow}>
              Export
            </Button>


            <Modal show={show} onHide={handleClose}>
              <Modal.Header closeButton>
                <Modal.Title>Export tree</Modal.Title>
              </Modal.Header>
              <Modal.Body>
              <Form.Group controlId="exampleForm.ControlTextarea1">
                  <Form.Label>JSON</Form.Label>
                  <Form.Control as="textarea" rows={3} defaultValue={resp} />
                </Form.Group>
              </Modal.Body>
              <Modal.Footer>
                <Button variant="secondary" onClick={handleClose}>
                  Close
                </Button>
              </Modal.Footer>
            </Modal>
          </>
        );

}
