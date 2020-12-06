import React, { useState } from "react";
import {Modal, Button, Container, Row, Col,Form,ButtonGroup} from "react-bootstrap";
import axios from 'axios'

export default function ModalAddPerson() {

      const [show, setShow] = useState(false);
      const handleClose = () => setShow(false);
      const handleShow = () => setShow(true);

      const [name, setName] = useState("");
    //  console.log(name);
      const [byear, setBY] = useState(0);
      const [dyear, setDY] = useState(0);
      const [mid, setMid] = useState(null);
      const [fid, setFid] = useState(null);
      const [gender, setGen] = useState(null);

      const content = {
          name: name,
          byear: byear,
          dyear: dyear,
          mid: mid,
          fid: fid,
          gender: gender
      }

      const sendAddPerson = () => {
        axios.post('/api/add_person', content)
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
            Add Person
          </Button>
          <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
              <Modal.Title>New Person</Modal.Title>
            </Modal.Header>
            <Modal.Body>
              <Form.Group controlId="Name">
                <Form.Label>First&Last Name</Form.Label>
                <Form.Control placeholder="Enter name" onChange={(e) => setName(e.target.value)} />
              </Form.Group>
              <Form.Group controlId="Parents" >
                <Form.Label>Choose gender &nbsp;</Form.Label>
                <Form.Control as="select" onChange={(e) => setGen(e.target.value)} custom>
                  <option>M</option>
                  <option>F</option>
                  </Form.Control>
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
              <Button variant="primary" onClick={() => {handleClose(); sendAddPerson();}}>
                Save Changes
              </Button>
            </Modal.Footer>
          </Modal>
        </>
      );


}
