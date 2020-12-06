import React, { useState } from "react";
import {Modal, Button, Container, Row, Col} from "react-bootstrap";
import {useDropzone} from 'react-dropzone';

export default function ModalImport() {

      const [show, setShow] = useState(false);
      const handleClose = () => setShow(false);
      const handleShow = () => setShow(true);

      const {getRootProps, getInputProps, open, acceptedFiles} = useDropzone({
          // Disable click and keydown behavior
          noClick: true,
          noKeyboard: true
        });

        const files = acceptedFiles.map(file => (
          <li key={file.path}>
            {file.path} - {file.size} bytes
          </li>
        ));

      return (
        <>
        <input {...getInputProps()} />
          <Button type="button" variant="light" onClick={open}>
            Import
          </Button>
          </>
      );


}
