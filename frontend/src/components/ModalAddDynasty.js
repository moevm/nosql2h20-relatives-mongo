import React, { useState } from "react";
import {Modal, Button, Container, Row, Col, Form} from "react-bootstrap";
import axios from 'axios'

export default function ModalAddDynasty() {

      const [show, setShow] = useState(false);
      const handleClose = () => setShow(false);
      const handleShow = () => setShow(true);

      const [dynasty, setDyn] = useState("");
      const [name, setName] = useState("");
    //  console.log(name);
      const [byear, setBY] = useState(0);
      const [dyear, setDY] = useState(0);
      const [mid, setMid] = useState(null);
      const [fid, setFid] = useState(null);

      const content = {
          dyn: dynasty,
          name: name,
          byear: byear,
          dyear: dyear,
          mid: mid,
          fid: fid,
      }

      const sendAddDyn = () => {
        axios.post('/api/add_dynasty', content)
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
      }

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
                <Form.Control placeholder="Enter dynasty name" onChange={(e) => setDyn(e.target.value)} />
                <Form.Group controlId="Name">
                  <Form.Label>First&Last Name</Form.Label>
                  <Form.Control placeholder="Enter founder name" onChange={(e) => setName(e.target.value)} />
                </Form.Group>
                  <Form.Group controlId="BY">
                    <Form.Label>Birth year</Form.Label>
                  </Form.Group>
                  <Form.Control placeholder="1900" onChange={(e) => setBY(e.target.value)}/>
                    <Form.Group controlId="DY">
                      <Form.Label>Death year</Form.Label>
                      <Form.Control placeholder="2000" onChange={(e) => setDY(e.target.value)}/>
                    </Form.Group>
                    <Form inline>
                      <Form.Group controlId="Parents">
                        <Form.Label>Mother &nbsp;</Form.Label>
                        <Form.Control placeholder="3" onChange={(e) => setMid(e.target.value)} custom>
                        </Form.Control>
                      </Form.Group>
                      <Form.Group controlId="Parents">
                        <Form.Label>&nbsp;Father&nbsp;</Form.Label>
                        <Form.Control placeholder="2" onChange={(e) => setFid(e.target.value)} custom >
                        </Form.Control>
                      </Form.Group>
                      </Form>
            </Modal.Body>
            <Modal.Footer>
              <Button variant="secondary" onClick={handleClose}>
                Close
              </Button>
              <Button variant="primary" onClick={() => {handleClose(); sendAddDyn();}}>
                Next
              </Button>
            </Modal.Footer>
          </Modal>
        </>
      );
}
