import React, { useState } from 'react';

type DataFetcherProps = {
  sourceName: string;
  render: (data: any) => React.ReactNode;
};

const fetchData = async (sourceName: string) => {
  const response = await fetch(`https://api.example.com/data/${sourceName}`);
  const data = await response.json();
  return {
    statusCode: response.status,
    bodyData: data.bodyData || {},
    errorMessage: data.errorMessage || '',
  };
};

const DataFetcher: React.FC<DataFetcherProps> = ({ sourceName, render }) => {
  const [loading, setLoading] = useState(false);
  const [dataState, setDataState] = useState<{
    statusCode: number | null;
    bodyData: any;
    errorMessage: string;
  }>({
    statusCode: null,
    bodyData: {},
    errorMessage: '',
  });

  const fetchDataForSource = async () => {
    setLoading(true);
    try {
      const result = await fetchData(sourceName);
      setDataState({
        statusCode: result.statusCode,
        bodyData: result.bodyData,
        errorMessage: result.errorMessage,
      });
    } catch (error) {
      setDataState({
        statusCode: 500,
        bodyData: {},
        errorMessage: 'Failed to fetch data',
      });
    } finally {
      setLoading(false);
    }
  };

  // Trigger data fetch on component mount (initial render)
  React.useEffect(() => {
    fetchDataForSource();
  }, [sourceName]); // Fetch data when sourceName changes

  return (
    <div>
      <h2>Data from {sourceName}</h2>
      {loading && <p>Loading...</p>}
      {dataState.statusCode === 200 && render(dataState.bodyData)}
      {dataState.statusCode && dataState.statusCode >= 400 && (
        <p>Error: {dataState.errorMessage}</p>
      )}
    </div>
  );
};

export default DataFetcher;