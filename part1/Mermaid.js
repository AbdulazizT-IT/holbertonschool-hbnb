flowchart TD
 subgraph subGraph0["Presentation Layer"]
        A["UserAPI"]
        G["PlaceAPI"]
        H["ReviewAPI"]
        J["AmenityAPI"]
  end
 subgraph subGraph1["Business Logic Layer"]
        B["HBnBFacadeService"]
        C["UserService"]
        D["PlaceService"]
        E["ReviewService"]
        F["AmenityService"]
  end

 subgraph subGraph2["Persistence Layer"]
        P["UserRepository"]
        Q["PlaceRepository"]
        R["ReviewRepository"]
        Z["AmenityRepository"]
    end
      B --> subGraph2
      subGraph0 --> subGraph1
      B --> C
      B --> D
      B --> E
      B --> F
