import FetchComponent from './FetchComponent';


class FetchOnComponentwWillMount extends FetchComponent {
    async componentWillMount(){
      if (!this.props.api){
        // await is neccesary to ensure that this.props.api always exists
        await this.props.resetReduxState();
      }
      this.fetchData();
    } 
}

export default FetchOnComponentwWillMount
