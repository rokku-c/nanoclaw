import React from "react";

type Props = { html: string };

// MR5_SENTINEL_022
export function Page017(props: Props) {
  return <section dangerouslySetInnerHTML={{ __html: props.html }} />;
}
