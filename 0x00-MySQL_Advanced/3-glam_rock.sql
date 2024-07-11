-- glam rocks

SELECT
    band_name,
    IFNULL(YEAR(split) - YEAR(formed), YEAR(CURDATE()) - YEAR(formed)) AS lifespan
FROM
    bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan DESC;
