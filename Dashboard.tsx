import React, { useState } from 'react';
import DataFetcher from './DataFetcher';

const Dashboard: React.FC = () => {
  const [formSubmitted, setFormSubmitted] = useState(false);

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setFormSubmitted(true);
  };

  const renderData = (bodyData: any) => {
    // Replace with your custom rendering logic based on bodyData
    return (
      <pre>{JSON.stringify(bodyData, null, 2)}</pre>
    );
  };

  return (
    <div>
      <h1>Data Dashboard</h1>
      <form onSubmit={handleSubmit}>
        <button type="submit">Fetch Data</button>
      </form>
      
      <DataFetcher sourceName="source1" render={renderData} />
      <DataFetcher sourceName="source2" render={renderData} />
      {/* Add more DataFetcher components for each data source */}
    </div>
  );
};

export default Dashboard;