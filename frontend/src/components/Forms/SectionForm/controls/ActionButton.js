import { Button, Tooltip } from "@mui/material";
import React from "react";
import { makeStyles } from "@mui/styles";

const useStyles = makeStyles({
  root: {
    minWidth: "0 !important",
  },
  //   secondary: {
  //     backgroundColor: theme.palette.secondary.light,
  //     "& .MuiButton-label": {
  //       color: theme.palette.secondary.main,
  //     },
  //   },
  primary: {
    "&.MuiButton-root": {
      backgroundColor: "#732d40",
      color: "#FFF",
    },

    "&.MuiButton-root:hover": {
      backgroundColor: "#73142d",
    },
  },
  secondary: {
    "&.MuiButton-root": {
      backgroundColor: "#b7bec9",
      color: "#000",
    },
    "&.MuiButton-root:hover": {
      backgroundColor: "#000",
      color: "#b7bec9",
    },
  },
});

export default function ActionButton(props) {
  const { variant, color, children, handleClick, tooltipTitle, ...others } =
    props;

  function CustomToolTip(props) {
    const { children, title } = props;

    return <Tooltip title={title}>{children}</Tooltip>;
  }

  const classes = useStyles();
  return tooltipTitle ? (
    <CustomToolTip title={tooltipTitle}>
      <Button
        variant={variant}
        className={`${classes.root} ${classes[color]}`}
        onClick={handleClick}
        {...others}
      >
        {children}
      </Button>
    </CustomToolTip>
  ) : (
    <Button
      variant={variant}
      className={`${classes.root} ${classes[color]}`}
      onClick={handleClick}
      {...others}
    >
      {children}
    </Button>
  );
}
