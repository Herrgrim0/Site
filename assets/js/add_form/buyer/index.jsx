import React from 'react';
import { connect } from 'react-redux';
import { Row, Col, Icon } from 'react-materialize';
import Scanner from './scanner';
import Entry from './entry';

class BuyerForm extends React.Component {
    static propTypes: {
        dispatch: React.PropTypes.func.isRequired,
        model: React.PropTypes.string.isRequired,
    }

    constructor(props) {
        super(props);

        this.state = {
            barcode: null, 
            scanner: false,
        };

        this.toggleScanner = this.toggleScanner.bind(this);
        this.barcodeScanned = this.barcodeScanned.bind(this);
    }

    barcodeScanned (barcode) {
        axios.get('/api/v1/check_membership/' + barcode)
            .then(json => {
                if (Array.isArray(json) && json.length == 1) {
                    this.setState({barcode: json[0]});
                }
            });
    }

    toggleScanner () {
         this.setState({
            scanner: !(this.state.scanner),
        });
    }

    render () {
        return (
            <div>
                <Row>
                    <h4>
                        <Icon>account_circle</Icon>
                        Acheteur
                    </h4>
                </Row>
                <Row>
                    <Col s={4}>
                        <Entry 
                            model={this.props.model}
                            barcode={this.state.barcode}
                        />
                    </Col>
                    <Col s={3}>
                        <a onClick={this.toggleScanner} className="waves-effect waves-light btn">
                            Scanner
                            <Icon right>
                                {this.state.scanner ? "videocam_off" : "videocam"}
                            </Icon>
                        </a>
                    </Col>
                </Row>
                {this.state.scanner ? <Scanner users={this.state.barcode} onDetected={this.barcodeScanned}/> : null}
            </div>
        );
    }
}

export default connect()(BuyerForm)
