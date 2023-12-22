from log import log_factory

log = log_factory(name=f"{__name__}")

if __name__ == "__main__":
    log.info(f"Starting...")
